package Model.Statements.SemaphoreStatements;

import Model.MyException;
import Model.ProgramState.*;
import Model.Statements.IStmt;
import Model.Triple;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Value.IntValue;
import Model.Value.Value;

import java.util.List;

public class AcquireStmt implements IStmt {
    private String var_id;

    public AcquireStmt(String id){
        var_id=id;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIStack<IStmt> stk= state.getStk();

        if (symTbl.isDefined(var_id)) {
            Type typId = (symTbl.lookup(var_id)).getType(); //getValue / lookup
            if (!typId.equals(new IntType()))
                throw new MyException("type of variable" + var_id + " is not int");
        } else throw new MyException("the used variable" + var_id + " is not in the sym table");

        int foundIndex = ((IntValue)symTbl.lookup(var_id)).getVal(); //we can downcast to IntValue because we know the type is int

        ISemaphoreTable sem = state.getSemaphoreTable();

        if(!sem.containsKey(foundIndex))
            throw new MyException("index "+ foundIndex + " not in the semaphoreTable");
        else
        {
            Triple<Integer, List<Integer>,Integer> triple = sem.getValue(foundIndex);
            int nl = triple.getSecond().size();
            if (triple.getFirst() - triple.getThird() > nl)
            {
                if(! triple.getSecond().contains(state.getId()))
                    triple.getSecond().add(state.getId());
            }
            else
                stk.push(this.dup());
        }

        return null;
    }

    @Override
    public IStmt dup() {
        return new AcquireStmt(var_id);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "acquire("+var_id+")";
    }
}
