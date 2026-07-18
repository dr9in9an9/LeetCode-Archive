/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (head == nullptr) {
            return head;
        }
        else {
            while (head->val == val) {
                if (head->next != nullptr) {
                    head = head->next;
                }
                else {
                    return nullptr;
                }
            }
            
            ListNode* curr = head;
            while (curr->next != nullptr) {
                if (curr->next->val == val) {
                    if (curr->next->next != nullptr) {
                        curr->next = curr->next->next;
                        if (curr->next->val != val) {
                            curr = curr->next;
                        }
                    }
                    else {
                        curr->next = nullptr;
                    }
                }
                else {
                    if (curr->next->val != val) {
                        curr = curr->next;
                    }
                }
            }
            return head;
        }
    }
};
