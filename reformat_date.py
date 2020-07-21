"""

Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
 

Example 1:

Input: date = "20th Oct 2052"
Output: "2052-10-20"
https://leetcode.com/problems/reformat-date/
"""

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        input_date = date.split(" ")

        month_dict = {'Mar': "03", 'Feb': "02", 'Aug': '08', 'Sep': '09', 'Apr': "04", 'Jun': "06", 'Jul': '07', 'Jan': '01', 'May': '05', 'Nov': '11', 'Dec': 12, 'Oct': 10}
        date = int(input_date[0][:-2]) 
        if date <= 9: 
            date = str(date).zfill(2) 

        return ("{}-{}-{}").format(input_date[2], month_dict[input_date[1]], date)

if __name__ == "__main__":
    a = Solution()
    print a.reformatDate("2th Oct 2052")
