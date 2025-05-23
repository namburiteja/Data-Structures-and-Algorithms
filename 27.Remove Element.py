	j = -1
        for i in range(len(nums)):
            if nums[i]==val:
                j = i
                break
        if j==-1:
            return len(nums)
        for i in range(j+1,len(nums)):
            if nums[i]!=val:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1    
        return j