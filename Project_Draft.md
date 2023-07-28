# Planeta Laser

## Indice

- [Planeta Laser](#planeta-laser)
  - [Indice](#indice)
  - [Controlador](#controlador)
  - [Vista](#vista)
  - [Modelo](#modelo)
    - [Tablas](#tablas)
    - [Tabla Clientes {#t\_clientes}](#tabla-clientes-t_clientes)

## Controlador

## Vista

## Modelo

### Tablas

| Tabla | Attributos |  |  |  |  |  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**Clientes**](#t_clientes) | Id | Nombre | Telefono | Mail | Descripcion |  |
| [**Proveedores**](#t_proveedores) | Id | Nombre | _Material_ | Telefono | Mail | Descripcion |
| [**Parametros**](#t_parametros) | Id | Nombre | Descripcion | Potencia | Velocidad |  |
| [**Productos**](#t_productos) | Id | Nombre | Descripcion | _Materiales_ |  |  |
| [**Materiales**](#t_materiales) | Id | Material | Descripcion | Medida | Stock |  |
| [**Pedidos**](#t_pedidos) | Id | _Cliente_ | _Producto_ | Fecha Pedido | Fecha Acordada | Fecha Entregado |

### Tabla Clientes {#t_clientes}
