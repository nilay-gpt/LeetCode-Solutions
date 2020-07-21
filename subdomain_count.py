"""
Example:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

https://leetcode.com/problems/subdomain-visit-count/
"""

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = {}
        for item in cpdomains:
            split = item.split(" ")
            count, domain_list = int(split[0]), split[1].split(".")

            for i in range(len(domain_list)):
                t = ".".join(domain_list[i:])

                if t not in domain_dict: domain_dict[t] = count
                else: domain_dict[t] += count

        return ["{} {}".format(value, key) for key, value in domain_dict.items()]

        
if __name__ == "__main__":
    a = Solution()
    print a.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
