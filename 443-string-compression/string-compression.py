class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer = 0  
        insert = 1
        while(pointer < len(chars)):
            group = 1
            while pointer + 1 < len(chars) and chars[pointer] == chars[pointer + 1]:
                group = group + 1
                pointer = pointer + 1
            
            # insert the value
            chars[insert - 1] = chars[pointer]

            if group > 1:
                group_string = str(group)
                chars[insert : insert + len(group_string)] = list(group_string)      
                insert = insert + len(group_string) + 1
            else:
                insert = insert + 1
            pointer = pointer + 1
        
        return insert - 1




#                       p
#   [ a a a b b c c c d v v]
      
#                     i
#   [ a 3 b 2 b c 3 d d v v]
#     0 1 2 3 4 5 6 7 8 9 10
#  g = 2
#   [a 2 b 2 c 3] = len --> 4