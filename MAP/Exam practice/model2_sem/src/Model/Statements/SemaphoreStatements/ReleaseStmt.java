package Model.Statements.SemaphoreStatements;

import Model.Expression.RelExp;
import Model.MyException;
import Model.ProgramState.ISemaphoreTable;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.PrgState;
import Model.Statements.IStmt;
import Model.Triple;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Value.IntValue;
import Model.Value.Value;

import java.util.List;

public class ReleaseStmt implements IStmt {
    private String var_id;

    public ReleaseStmt(String var){
        var_id = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
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
            if(triple.getSecond().contains(state.getId()))
            {
                    triple.getSecond().remove(state.getId());
            }

        }


        return null;
    }

    @Override
    public IStmt dup() {
        return new ReleaseStmt(var_id);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "release(" + var_id + ")";
    }
}
