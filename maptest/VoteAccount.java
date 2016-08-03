package maptest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.Map.Entry;
public class VoteAccount{
	public static void main(String[] args) {
		String[] voteStr = new String[]{"Mr.A","Mr.B","Mr.C","Mr.B","Mr.B","Mr.C","Mr.C","Mr.E","Mr.B","Mr.B","Mr.D","Mr.A","Mr.B"};
		TreeMap<String, Integer> voteMap = new TreeMap<String, Integer>();
		Arrays.sort(voteStr);
//		for(String votePeople: voteStr){
//		System.out.println(votePeople);
//		}
		voteMap.put(voteStr[0], 1);
		for(int i = 1; i < voteStr.length; i++){
			 if (!voteMap.containsKey(voteStr[i])) {
				 voteMap.put(voteStr[i], 1);
	            } else {
	                int count = voteMap.get(voteStr[i]) + 1;
	                voteMap.put(voteStr[i], count);
	            }
		}
		 List<Map.Entry<String,Integer>> list = new ArrayList<Map.Entry<String,Integer>>(voteMap.entrySet());
		 Collections.sort(list,new Comparator<Map.Entry<String,Integer>>() {
	            //升序排序
	            public int compare(Entry<String, Integer> o1,Entry<String, Integer> o2) {
	                return o2.getValue().compareTo(o1.getValue());
	            }
	            
	        });
		        for(Map.Entry<String,Integer> mapping:list){ 
		        	System.out.println(mapping.getKey()+":"+mapping.getValue()); 
        }  
	}
}

//for(int i = 0; i <voteStr.length; i++){
//voteMap.put(voteStr[i], 1 + "1");
////if(voteMap)
//}