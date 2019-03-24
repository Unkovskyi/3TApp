create table currency
(
  code text primary key not null,
  name text null
);

create table provider
(
  code text primary key not null,
  name text not null
);

create table currency_exchange_rate
(
  from_currency text not null ,
  to_currency text not null ,
  on_date numeric not null ,
  provider text not null,
  rate real not null check ( rate > 0.0 ),

  foreign key (from_currency) references currency(code),
  foreign key (to_currency) references currency(code),
  foreign key (provider) references provider(code),
  unique (from_currency, to_currency, provider, on_date)
);