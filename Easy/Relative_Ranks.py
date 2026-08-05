class Solution:   
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #[elem, ...] -> [[elem, og pos], ...]
        heap = []
        for i in range(0, len(score)):
            newest = [score[i], i]
            if heap:
                nex = len(heap) - 1
                while nex >= 0 and heap[nex][0] > newest[0]:
                    nex -= 1
                if nex == len(heap) - 1:
                    heap.append(newest)
                else:
                    heap.insert(nex + 1, newest)
            else:
                heap.append(newest)

        for i in range(0, len(heap)):
            if i < 3:
                match i:
                    case 0:
                        medal = "Gold Medal"
                    case 1:
                        medal = "Silver Medal"
                    case 2:
                        medal = "Bronze Medal"
                score[heap.pop()[1]] = medal
            else:
                score[heap.pop()[1]] = str(i + 1)
        return score
