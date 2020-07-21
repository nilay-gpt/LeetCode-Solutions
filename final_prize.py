"""
"""


class Solution(object):
    def finalpricess(self, pricess):
        discount_list = []
        for i in range(len(pricess)):
            inserted = False
            for j in range(i+1, len(pricess)):
                if pricess[i] >= pricess[j]:
                    inserted = True
                    discount_list.append(pricess[i] -  pricess[j])
                    break
            if not inserted:
                discount_list.append(pricess[i])

        return discount_list




if __name__ == "__main__":
    a = Solution()
    print a.finalpricess([10,1,1,6])
