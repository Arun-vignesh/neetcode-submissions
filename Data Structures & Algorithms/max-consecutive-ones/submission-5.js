class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let consecutiveValueFinal=0;
        let consecutiveValue=0;
        for(let i=0;i< nums.length;i++){
            if(nums[i]===1){
                consecutiveValue +=1;
            }else{
                if(consecutiveValue> consecutiveValueFinal){
                    consecutiveValueFinal = consecutiveValue
                }
                consecutiveValue = 0;
            }
        }
        if(consecutiveValue> consecutiveValueFinal){
                    consecutiveValueFinal = consecutiveValue
        }
        return consecutiveValueFinal;
    }
}
