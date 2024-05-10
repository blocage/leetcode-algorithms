import appEvents from '../service/appEvents.js';
import eventify from 'ngraph.events';

export default windowCollectionModel();

function windowCollectionModel() {

  appEvents.showNodeListWindow.on(showWindow);
  appEvents.hideNodeListWindow.on(hideWindow);

  var api = {
    getWindows: getWindows
  };

  var registeredWindows = Object.create(null);
  var allWindows = [];

  eventify(api);

  return api;

  function getWindows() {
    return allWindows;
  }

  function showWindow(viewModel, windowId) {
    var windowIndex = registeredWindows[windowId];
    if (windowIndex === undefined) {
      allWindows.push(viewModel);
      windowIndex = registeredWindows[windowId] = allWindows.length - 1;
    } else {
      allWindows[windowIndex] = viewModel;
    }
    api.fire('changed');
  }

  function hideWindow(windowId) {
    var windowIndex = registeredWindows[windowId];
    if (windowIndex !== undefined) {
      delete registeredWindows[windowId];
      allWindows.splice(windowIndex, 1);

      api.fire('changed', windowIndex);
    }
  }
}
