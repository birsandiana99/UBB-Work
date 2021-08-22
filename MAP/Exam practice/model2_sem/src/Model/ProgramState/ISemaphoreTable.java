package Model.ProgramState;

import Model.Triple;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public interface ISemaphoreTable {
    public Collection<Integer> keys();
    public boolean containsKey(int k);
    public void replace(int k, Triple<Integer, List<Integer>,Integer> triple);
    public Triple<Integer, List<Integer>,Integer> getValue(int k);
    public Collection<Triple<Integer, List<Integer>,Integer>> values();
    public void setContent(Map<Integer,Triple<Integer, List<Integer>,Integer>> map);
    public Map<Integer, Triple<Integer, List<Integer>,Integer>> getContent();

    public void add(Triple<Integer, List<Integer>,Integer> triple);
    public int getAddr();

    /*
    public boolean isDefined(K id);
    public void update (K id, V val);
    public void add(K id, V val);
    public void remove(K id);
    public V lookup(K id);
    public Collection<V> values();
    public MyIDictionary<K,V> dup();
    public ConcurrentHashMap<K,V> getAll();
    public Collection<K> keys();
    */
}
