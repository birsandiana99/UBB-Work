package core.model;

import lombok.*;

import javax.persistence.*;

@Entity
@IdClass(ClientSalePk.class)
@Table(name = "sales")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@EqualsAndHashCode
@Builder
public class Sales {
    @Id
    @ManyToOne(optional = false, fetch = FetchType.EAGER)
    @JoinColumn(name = "booksid")
    private Books book;

    @Id
    @ManyToOne(optional = false, fetch = FetchType.EAGER)
    @JoinColumn(name = "clientsid")
    private Clients client;

    @Override
    public String toString() {
        return "Sales{" +
                "book=" + book.getId() +
                ", client=" + client.getId() +
                '}';
    }
}
