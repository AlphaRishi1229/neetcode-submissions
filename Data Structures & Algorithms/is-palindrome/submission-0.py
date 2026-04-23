class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1, ptr2 = 0, len(s) - 1
        while ptr1 < ptr2:
            ord_at_ptr1 = ord(s[ptr1].lower())
            ord_at_ptr2 = ord(s[ptr2].lower())
            if not (
                (
                    ord_at_ptr1 >= ord('a')
                    and ord_at_ptr1 <= ord('z')
                ) or (
                    ord_at_ptr1 >= ord('0')
                    and ord_at_ptr1 <= ord('9')
                )
            ):
                ptr1 += 1
                continue
            
            if not (
                (
                    ord_at_ptr2 >= ord('a')
                    and ord_at_ptr2 <= ord('z')
                ) or (
                    ord_at_ptr2 >= ord('0')
                    and ord_at_ptr2 <= ord('9')
                )
            ):
                ptr2 -= 1
                continue

            if ord_at_ptr1 != ord_at_ptr2:
                return False

            ptr1 += 1
            ptr2 -= 1

        return True
