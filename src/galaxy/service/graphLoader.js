import config from '../../config.js';
import request from './request.js';
import createGraph from './graph.js';
import appEvents from './appEvents.js';
import appConfig from '../native/appConfig.js';
import asyncFor from 'rafor';
import Promise from 'bluebird';

export default loadGraph;

/**
 * @param {string} name of the graph to be downloaded
 * @param {progressCallback} progress notifies when download progress event is
 * received
 * @param {completeCallback} complete notifies when all graph files are downloaded
 *
 */
function loadGraph(name, progress) {
  var positions, labels;
  var outLinks = [];
  var inLinks = [];

  // todo: handle errors
  var manifestEndpoint = config.dataUrl + name;
  var galaxyEndpoint = manifestEndpoint;

  var manifest;

  return loadManifest()
    .then(loadPositions)
    .then(loadLinks)
    .then(loadLabels)
    .then(convertToGraph);

  function convertToGraph() {
    return createGraph({
      positions: positions,
      labels: labels,
      outLinks: outLinks,
      inLinks: inLinks
    });
  }

  function loadManifest() {
    return request(manifestEndpoint + '/manifest.json?nocache=' + (+new Date()), {
      responseType: 'json'
    }).then(setManifest);
  }

  function setManifest(response) {
    manifest = response;
    var version = getFromAppConfig(manifest) || manifest.last;
    if (manifest.endpoint) {
      // the endpoint is overridden. Since we trust manifest endpoint, we also
      // trust overridden endpoint:
      galaxyEndpoint = manifest.endpoint;
    } else {
      galaxyEndpoint = manifestEndpoint;
    }
    galaxyEndpoint += '/' + version;
    appConfig.setManifestVersion(version);
  }

  function getFromAppConfig(manifest) {
    var appConfigVersion = appConfig.getManifestVersion();
    var approvedVersions = manifest && manifest.all;

    // default to the last version:
    if (!approvedVersions || !appConfigVersion) return;

    // If this version is whitelisted, let it through:
    if (approvedVersions.indexOf(appConfigVersion) >= 0) {
      return appConfigVersion;
    }
  }

  function loadPositions() {
    return request(galaxyEndpoint + '/positions.json', {
      responseType: 'json',
      progress: reportProgress(name, 'positions')
    }).then(setPositions);
  }

  function setPositions(buffer) {
    positions = new Int32Array(buffer['data']);
    var scaleFactor = appConfig.getScaleFactor();
    for (var i = 0; i < positions.length; ++i) {
      positions[i] *= scaleFactor;
    }
    appEvents.positionsDownloaded.fire(positions);
  }

  function loadLinks() {
    return request(galaxyEndpoint + '/links.json', {
      responseType: 'json',
      progress: reportProgress(name, 'links')
    }).then(setLinks);
  }

  function setLinks(buffer) {
    var links = new Int32Array(buffer['data']);
    var lastArray = [];
    outLinks[0] = lastArray;
    var srcIndex;
    var processed = 0;
    var total = links.length;

    asyncFor(links, processLink, reportBack);
    var deffered = defer();
    function processLink(link) {
      if (link < 0) {
        srcIndex = -link - 1;
        lastArray = outLinks[srcIndex] = [];
      } else {
        var toNode = link - 1;
        lastArray.push(toNode);
        if (inLinks[toNode] === undefined) {
          inLinks[toNode] = [srcIndex];
        } else {
          inLinks[toNode].push(srcIndex);
        }
      }
      processed += 1;
      if (processed % 10000 === 0) {
        reportLinkProgress(processed / total);
      }
    }

    function reportLinkProgress(percent) {
      progress({
        message: name + ': initializing edges ',
        completed: Math.round(percent * 100) + '%'
      });
    }

    function reportBack() {
      appEvents.linksDownloaded.fire(outLinks, inLinks);
      deffered.resolve();
    }

    return deffered.promise;
  }

  function loadLabels() {
    return request(galaxyEndpoint + '/labels.json', {
      responseType: 'json',
      progress: reportProgress(name, 'labels')
    }).then(setLabels);
  }

  function setLabels(data) {
    labels = data;
    appEvents.labelsDownloaded.fire(labels);
  }

  function reportProgress(name, file) {
    return function(e) {
      let progressInfo = {
        message: name + ': downloading ' + file,
      };
      if (e.percent !== undefined) {
        progressInfo.completed = Math.round(e.percent * 100) + '%'
      } else {
        progressInfo.completed = Math.round(e.loaded) + ' bytes'
      }
      progress(progressInfo);
    };
  }
}

function defer() {
    var resolve, reject;
    var promise = new Promise(function() {
        resolve = arguments[0];
        reject = arguments[1];
    });
    return {
        resolve: resolve,
        reject: reject,
        promise: promise
    };
}
