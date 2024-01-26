class Solution {
    fun longestPalindrome(s: String): String {

        var temp = ""

        for (i in s.length downTo 0) {
            for (j in 0 .. s.length - i) {
                temp = s.substring(j, j + i)
                if (temp.reversed() == temp) return temp
            }
        }

        return s.substring(0, 1)
    }
}