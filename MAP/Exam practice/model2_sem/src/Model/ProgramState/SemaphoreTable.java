package Model.ProgramState;


import Model.Triple;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class SemaphoreTable implements ISemaphoreTable {
    //private ConcurrentHashMap<Integer, Triple<Integer, List<Integer>,Integer>> semTable ; //???????? TODO
    private Map<Integer, Triple<Integer, List<Integer>,Integer>> semTable ;
    private Integer index;

    public SemaphoreTable(){
        //semTable = new ConcurrentHashMap<Integer, Triple<Integer, List<Integer>,Integer>>();
        semTable = new ConcurrentHashMap<>();
        index=0;
    }


    @Override
    public Collection<Integer> keys() {
        return semTable.keySet();
    }

    @Override
    public boolean containsKey(int k) {
        return semTable.containsKey(k);
    }

    @Override
    public void replace(int k, Triple<Integer, List<Integer>, Integer> triple) {
        semTable.replace(k,triple);
    }

    @Override
    public Triple<Integer, List<Integer>, Integer> getValue(int k) {
        return semTable.get(k);
    }

    @Override
    public Collection<Triple<Integer, List<Integer>, Integer>> values() {
        return semTable.values();
    }

    @Override
    public void setContent(Map<Integer, Triple<Integer, List<Integer>, Integer>> map) {
        semTable=map;
    }

    @Override
    public Map<Integer, Triple<Integer, List<Integer>, Integer>> getContent() {
        return semTable;
    }

    @Override
    public synchronized void add(Triple<Integer, List<Integer>, Integer> triple) {
        index++;
        semTable.put(index, triple);
    }

    @Override
    public int getAddr() {
        return index;
    }

    @Override
    public String toString() {
        return semTable.toString();
    }
}
