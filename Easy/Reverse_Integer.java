class Solution {
    public int reverse(int x) {
        String str = "";
        boolean neg = false;

        if (x < 0) {
            x *= -1;
            neg = true;
        }

        str += x;
        int rev = 0;

        for (int i = str.length() - 1; i >= 0; i--) {
            int temp = ((int) str.charAt(i)) - 48;
            
            rev += (temp * Math.pow(10, i));

            if (Math.pow(-2, 31) >= rev || rev >= Math.pow(2, 31) - 1) {
                return 0;
            }
        }

        if (neg) {
            rev *= -1;
        }

        return rev;
    }
}
