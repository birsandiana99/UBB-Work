package Model.Expression;

import Model.MyException;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.MyIHeap;
import Model.Type.BoolType;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.Value;

public class MulExp implements Exp {
    private Exp exp1;
    private Exp exp2;

    public MulExp(Exp e1, Exp e2){
        exp1=e1;
        exp2=e2;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Value> heap) throws MyException {
        int res=0;
        Value v1,v2;
        v1=exp1.eval(tbl,heap);
        if(v1.getType().equals(new IntType())) {
            v2 = exp2.eval(tbl,heap);
            if (v2.getType().equals(new IntType())) {
                //both operands are int, now evaluate the exp
                IntValue b1 = (IntValue) v1;
                IntValue b2 = (IntValue) v2;

                res = (b1.getVal()*b2.getVal())-(b1.getVal()+b2.getVal());

                Value val_final = new IntValue(res);
                return val_final;
            } else
                throw new MyException("Operand 2 not int, mulexp: " + this.toString());
        }
        else
            throw new MyException("Operand 1 not int, mulexp: " + this.toString());
    }

    @Override
    public Exp dup() {
        return new MulExp(exp1.dup(),exp2.dup());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typ1, typ2;
        typ1=exp1.typecheck(typeEnv);
        typ2=exp2.typecheck(typeEnv);
        if (typ1.equals(new IntType())) {
            if (typ2.equals(new IntType())) {
                return new IntType();
            } else
                throw new MyException("second operand is not an integer" + " \n mul expression: " + this.toString());
        }else
            throw new MyException("first operand is not an integer"+ " \n mul expression: " + this.toString());
    }

    @Override
    public String toString() {
        return "MUL(" + exp1.toString()+ "," +exp2.toString() + ")";
    }
}
