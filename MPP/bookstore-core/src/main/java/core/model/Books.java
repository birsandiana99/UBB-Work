package core.model;

import lombok.*;
import org.hibernate.mapping.Collection;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Data
@Builder
public class Books extends BaseEntity<Long> {
    @Column(name = "title", nullable =false)
    private String title;

    @Column(name = "author", nullable =false)
    private String author;

    @Column(name = "price", nullable =false)
    private Integer price;

    @OneToMany(mappedBy = "book", orphanRemoval = true, cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<Sales> sales = new ArrayList<>();

    public List<Clients> getClients(){
        return Collections.unmodifiableList(sales.stream()
        .map(e->e.getClient()).collect(Collectors.toList()));
    }

    public void addSale(Sales sale){
        sales.add(sale);
    }

    @Override
    public String toString() {
        return "Books{" +
                "title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", price=" + price +
                ", sales=" + sales +
                '}'+super.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Books that = (Books) o;

        return title.equals(that.title);
    }

    @Override
    public int hashCode() {
        return title.hashCode();
    }
}
