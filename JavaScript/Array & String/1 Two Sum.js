/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const pairIndex={};

    for(let i=0;i<nums.length;i++){
        const num1=nums[i];
        const num2=target-num1
        if (num2 in pairIndex){
            return ([i,pairIndex[num2]]);
        }
        pairIndex[num1]=i;
    }
}