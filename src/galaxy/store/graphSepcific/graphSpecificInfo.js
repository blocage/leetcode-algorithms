export default graphSpecificInfo;

function graphSpecificInfo(graphName) {
  switch(graphName) {
    case 'leetcode':
      return new PackagesGraph(graphName);
  }
  return new DefaultGraph(graphName);
}

function DefaultGraph(graphName) {
  this.graphName = graphName;
  this.getInDegreeLabel = function getInDegreeLabel(inDegreeValue) {
    return 'in-degree';
  };

  this.getOutDegreeLabel = function getInDegreeLabel(outDegreeValue) {
    return 'out-degree';
  };
}

function PackagesGraph(graphName) {
  DefaultGraph.call(this, graphName);

  this.getInDegreeLabel = function getInDegreeLabel(inDegreeValue) {
    return inDegreeValue === 1 ? 'solution' : 'solutions';
  };

  this.getOutDegreeLabel = function getInDegreeLabel(outDegreeValue) {
    return outDegreeValue === 1 ? 'dependency' : 'dependencies';
  };
}

function GoGraph(graphName) {
  PackagesGraph.call(this, graphName);
}

function FollowersGraph(graphName) {
  DefaultGraph.call(this, graphName);

  this.getInDegreeLabel = function getInDegreeLabel(inDegreeValue) {
    return inDegreeValue === 1 ? 'follower' : 'followers';
  };

  this.getOutDegreeLabel = function getInDegreeLabel(outDegreeValue) {
    return 'following';
  };
}
