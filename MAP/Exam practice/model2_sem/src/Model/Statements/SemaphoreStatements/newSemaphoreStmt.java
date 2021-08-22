package Model.Statements.SemaphoreStatements;

import Model.Expression.Exp;
import Model.MyException;
import Model.ProgramState.*;
import Model.Statements.IStmt;
import Model.Triple;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Value.IntValue;
import Model.Value.Value;

import java.util.ArrayList;
import java.util.List;

public class newSemaphoreStmt implements IStmt {
    private String var_id;
    private Exp exp1;
    private Exp exp2;

    public newSemaphoreStmt(String var, Exp e1, Exp e2){
        var_id=var; exp1=e1; exp2=e2;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        int n1 = ((IntValue)exp1.eval(symTbl,heap)).getVal();
        int n2 = ((IntValue)exp2.eval(symTbl,heap)).getVal();

        ISemaphoreTable sem = state.getSemaphoreTable();

        sem.add(new Triple<>(n1, new ArrayList<>(), n2));

        if (symTbl.isDefined(var_id)) {
            Type typId = (symTbl.lookup(var_id)).getType(); //getValue / lookup
            if (typId.equals(new IntType()))
                symTbl.update(var_id, new IntValue(sem.getAddr()));
            else
                throw new MyException("variable " + var_id + " not int type");
        } else throw new MyException("variable " + var_id + " does not exist in the sym table");


        return null;
    }

    @Override
    public IStmt dup() {
        return new newSemaphoreStmt(var_id,exp1.dup(),exp2.dup());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "newSemaphore(" + var_id + "," + exp1.toString() + "," + exp2.toString() + ")";
    }
}
