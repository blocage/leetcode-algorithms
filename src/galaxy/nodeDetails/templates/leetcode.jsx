import React from 'react';
import commonPackageTemplate from './commonPackageTemplate.jsx';

export default require('maco').template(leetcode, React);

function leetcode(props) {
  var model = props.model;

  var link = 'https://github.com/blocage/leetcode-algorithms/tree/main/' + encodeURIComponent(model.name);
  var linkText = model.name;

  return commonPackageTemplate(model, link, linkText);
}
