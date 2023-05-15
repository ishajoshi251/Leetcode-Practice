/**
 * @param {number} millis
 */
async function sleep(millis) {
    let t=Date.now();
    let newT=millis+t;
    while(Date.now()<newT){
	   // blocked the main thread
    }
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */