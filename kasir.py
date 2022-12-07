#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from tabulate import tabulate


# In[2]:


class Transaction:
    
    def __init__(self):
        ''' fungsinya untuk menginisiasi dictionary'''
        self.shoppingcart = dict()
    
    def add_item(self, item, quantity, price):
        '''fungsi menambahkan item belanja
        parameternya
            item (str)    : item belanja yang akan ditambahkan, key dalam dictionary shoppingcart
            quantity (int): jumlah item belanja
            price (int)   : harga per pieces item belanja'''
        
        #cek kesesuaian type data input
        if type(item) !=str:
            print('Nama Item harus dalam bentuk teks.')
            
        elif type(quantity) !=int:
            print('Jumlah Item harus dalam bentuk angka.')
            
        elif type(price) !=int:
            print('Harga Item harus dalam bentuk angka.')
            
        else:
            self.shoppingcart.update({item : [quantity, price, quantity*price]})
            print(f'Berhasil menambahkan : {item} dengan jumlah {quantity}pcs dengan harga Rp {price}.')
    
    def update_item(self, item, item_baru):
        '''fungsi untuk mengubah nama item barang yang akan dibeli
        parameternya
        item (str)      :nama item yang akan diganti
        item_baru (str) :nama item baru'''
        
        try:
            temp = self.shoppingcart[item]
            self.shoppingcart.pop(item)
            self.shoppingcart.update({item_baru: temp})
            
            print('Berikut adalah daftar belanja anda :')
            self.check_transaksi()
            print("")
            print(f'Berhasil mengubah Nama Item {item} menjadi {item_baru}.')
            
        except KeyError:
            print(f'Item {item} yang anda masukkan tidak ada dalam daftar pembelian.')
       
    def update_quantity(self, item, quantity_baru):
        '''fungsi untuk mengubah jumlah item barang yang akan dibeli
        parameternya
        quantity (str)      : jumlah item yang akan diganti
        quantity_baru (str) : jumlah item baru'''
        
        try:               
            self.shoppingcart[item][0] = quantity_baru
            self.shoppingcart[item][2] = quantity_baru*self.shoppingcart[item][1]
            
            print('Berikut adalah daftar belanja anda :')
            self.check_transaksi()
            print("")
            print(f'Berhasil mengubah Jumlah Item {item} menjadi {quantity_baru}pcs.') 
        
        except KeyError:
            print('Item yang anda masukkan tidak ada dalam daftar pembelian.')
            
        except ValueError:
            print('Item yang anda masukkan harus dalam bentuk angka.')    
        
    def update_price(self, item, price_baru):
        '''fungsi untuk mengubah harga item pembelian
        parameternya
        price (int)      : harga item yang akan diganti
        price_baru (int) : harga item baru'''
        
        try:
            self.shoppingcart[item][1] = price_baru
            self.shoppingcart[item][2] = price_baru*self.shoppingcart[item][0]
            
            print('Berikut adalah daftar belanja anda :')
            self.check_transaksi()
            print("")
            print(f'Berhasil mengubah Harga Item {item} menjadi Rp {price_baru}.')
            
        except KeyError:
            print('Item  masukkan tidak ada dalam daftar pembelian.')   
        
    def delete_item(self, item):
        '''fungsi untuk menghapus data pembelian yang sudah terinput sebelumnya,
        yang dihapus meliputi nama item, quantity dan harga item tersebut.
        parameternya
        item (str): nama item yang akan dihapus'''
        try:
            self.shoppingcart.pop(item)
        
            print('Berikut adalah daftar belanja anda :')
            self.check_transaksi()
            print("")
            print(f'Berhasil menghapus item {item} dari daftar pembelian.')
            
        except KeyError:
            print('Item  masukkan tidak ada dalam daftar pembelian.') 
        
    def reset_transaksi(self):
        '''fungsinya untuk menghapus semua data pembelian'''
        
        self.shoppingcart.clear()
        print('Semua pembelian berhasil dihapus')
        
    def check_transaksi(self):
        '''fungsinya mengecek keseluruhan pembelian yang tersimpan di dictionary transaksi.'''
        
        if self.shoppingcart == dict():
            print('Belum ada pembelian.')
        
        else:
            table_transaksi = pd.DataFrame(self.shoppingcart).T
            headers = ['Nama Barang', 'Jumlah', 'Harga per pcs', 'Total Harga']
            print(tabulate(table_transaksi, headers, tablefmt="github"))
    
    def total_transaksi(self):
        '''fungsinya untuk menampilkan harga setelah terpotong diskon sesuai total pembelian'''
        
        total_price = 0
        for item in self.shoppingcart:
            total_price += self.shoppingcart[item][2]
            
        if total_price <= 300_000 and total_price > 200_000:
            discount =int(0.05 * total_price)
            total_price_discounted =int(total_price - discount)
            
        elif total_price <= 500_000 and total_price > 300_000:
            discount =int(0.08 * total_price)
            total_price_discounted =int(total_price - discount)
            
        elif total_price > 500_000:
            discount =int(0.1 * total_price)
            total_price_discounted =int(total_price - discount)
        else:
            total_price_discounted = total_price
            
        print('Berikut adalah daftar belanja anda :')    
        self.check_transaksi()
        print("")
        print(f'Total harga yang harus anda bayar setelah dipotong diskon (jika ada) sebesar Rp {total_price_discounted}')


# In[ ]:




