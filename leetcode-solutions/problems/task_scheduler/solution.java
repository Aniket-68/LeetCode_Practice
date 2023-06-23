class Solution {
    public int leastInterval(char[] tasks, int n) {
         int charfreq[]=new int[26];
         int maxfreq=0;

         for(int i=0;i<tasks.length;i++){
            charfreq[tasks[i]-'A']++;
            maxfreq=Math.max(maxfreq,charfreq[tasks[i]-'A']);
         }

         int maxfreqcount=0;

         for(int i=0;i<26;i++){
             if(charfreq[i]==maxfreq)
             maxfreqcount++;
         }

         int result=(1+n)*(maxfreq-1)+maxfreqcount;
         result= Math.max(tasks.length,result);
        return result;
    }
}