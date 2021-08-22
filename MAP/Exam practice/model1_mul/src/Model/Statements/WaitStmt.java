package Model.Statements;

import Model.Expression.ValueExp;
import Model.MyException;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.MyIHeap;
import Model.ProgramState.MyIStack;
import Model.ProgramState.PrgState;
import Model.Type.Type;
import Model.Value.IntValue;
import Model.Value.Value;

public class WaitStmt implements IStmt {
    private int nr;

    public WaitStmt(int n){
        nr=n;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTlb = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        MyIStack<IStmt> stk = state.getStk();

        if(nr != 0)
        {
            //stk.push(new PrintStmt(new ValueExp(new IntValue(nr))));
            //stk.push(new WaitStmt(nr-1));
            stk.push(new WaitStmt(nr-1));
            stk.push(new PrintStmt(new ValueExp(new IntValue(nr))));

        }

        return null;
    }

    @Override
    public IStmt dup() {
        return new WaitStmt(nr);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "WAIT(" + nr + ")";
    }
}
