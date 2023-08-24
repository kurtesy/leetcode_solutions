class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        i = 0
        line_len_counter = 0
        word_count_in_line = 0

        while i < len(words):
           # current line
           line = []
           incr = len(words[i])

           # keep iterating as long as we have not bypassed the maxWidth
           while i < len(words) and line_len_counter + incr <= maxWidth:
               
               line.append(" " + words[i])
               line_len_counter+=incr
               word_count_in_line+=1
               # go to next word
               i+=1
               if i == len(words):
                   break
           # find words included in the line each word (except first word) will have atleast one
           # space attached to it hence the "+ 1" in increment 
               incr = len(words[i]) + 1

           # remove space in first word
           line[0]=line[0][1:]

           # extra space needed to be added
           extra_space_needed_count = maxWidth - line_len_counter

           # if there's only one word in line or it's last line
           if i == len(words) or word_count_in_line == 1:
               line+=" "*extra_space_needed_count
               output.append("".join(line))
           else:
               # for i%n range of is [0-n − 1]
               # to start modulo by m, simply use the formula: (i%(n-m))+m
               # hence (z%(word_count_in_line-1)) + 1 range is [1,word_count-1]
               for z in range(0,extra_space_needed_count):
                    line[(z%(word_count_in_line-1)) + 1] = " " + line[(z%(word_count_in_line-1)) + 1]
                    print((z%(word_count_in_line-1)) + 1)
               output.append("".join(line))

           # reset counters and reset the line  
           line_len_counter = 0
           word_count_in_line = 0
           line = []

        return output
  

               

                