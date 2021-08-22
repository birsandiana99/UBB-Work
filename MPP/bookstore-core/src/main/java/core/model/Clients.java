package core.model;

import lombok.*;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class Clients extends BaseEntity<Long> {
    @Column(name="name", nullable = false)
    private String name;

    @Column(name = "moneyspent",nullable = false)
    private Integer moneySpent = 0;

    @OneToMany(mappedBy = "client", orphanRemoval = true, cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<Sales> sales = new ArrayList<>();

    public List<Books> getBooks(){
        return Collections.unmodifiableList(sales.stream().map(s->s.getBook()).collect(Collectors.toList()));
    }

    public void addSale(Sales sale){
        sales.add(sale);
        this.moneySpent += sale.getBook().getPrice();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Clients that = (Clients) o;

        return name.equals(that.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }

    @Override
    public String toString() {
        return "Clients{" +
                "name='" + name + '\'' +
                ", moneySpent=" + moneySpent +
                ", sales=" + sales +
                '}'+super.toString();
    }
}
