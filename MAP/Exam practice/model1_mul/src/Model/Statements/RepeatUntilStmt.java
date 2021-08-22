package Model.Statements;

import Model.Expression.Exp;
import Model.Expression.NotExp;
import Model.MyException;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.MyIHeap;
import Model.ProgramState.MyIStack;
import Model.ProgramState.PrgState;
import Model.Type.BoolType;
import Model.Type.Type;
import Model.Value.BoolValue;
import Model.Value.Value;

public class RepeatUntilStmt implements IStmt {
    private IStmt stmt;
    private Exp exp;

    public RepeatUntilStmt(IStmt st, Exp e){
        stmt=st;
        exp=e;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getStk();
        IStmt newStmt = new CompStmt(stmt, new WhileStmt(new NotExp(exp),stmt.dup()));
        stk.push(newStmt);
        return null;

    }

    @Override
    public IStmt dup() {
        return new RepeatUntilStmt(stmt.dup(),exp.dup());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "repeat " + stmt.toString() + " until " + exp.toString();
    }
}
