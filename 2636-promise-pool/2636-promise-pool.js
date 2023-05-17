/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    const results = [];
  let currentIndex = 0;

  const executeNextFunction = async () => {
    if (currentIndex >= functions.length) 
    {
      return;
    }

    const func = functions[currentIndex];
    currentIndex++;

    const result = await func();
    results.push(result);

    await executeNextFunction();
      
  };

 
const promises = [];
  for (let i = 0; i < n; i++) 
  {
    promises.push(executeNextFunction());
  }

  await Promise.all(promises);
    
  return [results, results[results.length - 1]];

    
};
/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */