#
# @lc app=leetcode.cn id=1410 lang=python
#
# [1410] HTML 实体解析器
#

# @lc code=start
class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """

        i = 0
        while i < len(text):
            if text[i] == '&':
                end_position = i
                while end_position < len(text) and text[end_position] != ';':
                    end_position += 1
                if end_position < len(text):
                    entity = text[i + 1:end_position]
                    if entity == 'amp':
                        text = text[:i] + '&' + text[end_position + 1:]
                    elif entity == 'lt':
                        text = text[:i] + '<' + text[end_position + 1:]
                    elif entity == 'gt':
                        text = text[:i] + '>' + text[end_position + 1:]
                    elif entity == 'quot':
                        text = text[:i] + '\"' + text[end_position + 1:]
                    elif entity == 'apos':
                        text = text[:i] + '\'' + text[end_position + 1:]
                    elif entity == "frasl":
                        text = text[:i] + '/' + text[end_position + 1:]
            i += 1
        return text

# @lc code=end

