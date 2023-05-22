/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) {
        return 'null';
  }
  if (typeof object === 'string') {
    
    return '"' + object + '"';
  }
  if (typeof object === 'number' || typeof object === 'boolean') {
    
    return String(object);
  }
  if (Array.isArray(object)) {
    
    const items = object.map(items => jsonStringify(items));
    return '[' + items.join(',') + ']';
  }
 
  if (typeof object === 'object') {
     const keys = Object.keys(object);
     const items = keys.map(key => '"' + key + '":' +      jsonStringify(object[key]));
     return '{' + items.join(',') + '}';
  }

    
};