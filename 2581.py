class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        connect_map = [[] for i in range(len(edges) + 1)]
        n = 0
        for i in range(len(edges)):
            [no1,no2] = edges[i]
            connect_map[no1].append(no2)
            connect_map[no2].append(no1)
            n = max(n,no1,no2)
        n = n +1
        new_guesses = [[] for i in range(len(edges)+1)]
        for i in range(len(guesses)):
            [fa,no] = guesses[i]
            new_guesses[fa].append(no)
        
        result = 0
        used = [0]*n
        used[0] = 1
        root_zero = self.check_0_root(connect_map,new_guesses,0,used)
        used = [0]*n
        used[0] = 1
        result = result + self.check_root(connect_map,new_guesses,0,k,root_zero,used)
        return result

    def check_0_root(self,connect_map,new_guesses,head,used):
        result = 0
        for i in range(len(connect_map[head])):
            target = connect_map[head][i]
            if used[target] == 1:
                continue
            if new_guesses[head].count(target) == 1:
                result = result + 1
            used[target] = 1
            result = result + self.check_0_root(connect_map,new_guesses,target,used)
        return result

    def check_root(self,connect_map,new_guesses,head,k,now_correct,used):
        result = 0
        if now_correct >= k:
            result = result + 1
    
        for i in range(len(connect_map[head])):
            target = connect_map[head][i]
            correct_num = now_correct
            if used[target] == 1:
                continue
            if new_guesses[head].count(target) == 1:
                correct_num = correct_num - 1
            if new_guesses[target].count(head) == 1:
                correct_num = correct_num + 1
            used[target] = 1
            result = result + self.check_root(connect_map,new_guesses,target,k,correct_num,used)
        return result
        
