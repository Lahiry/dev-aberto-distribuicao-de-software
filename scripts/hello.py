#!/usr/bin/env python3
import dev_aberto

if __name__ == '__main__':
    date, name = dev_aberto.hello()
    print('Último commit feito em:', date, ' por', name)
