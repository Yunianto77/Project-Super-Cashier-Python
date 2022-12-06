# Project-Super-Cashier-Python
Resporitory ini berisi Project Super Cashier menggunakan bahasa pemrograman python.

## Background
 Aplikasi sederhana Super Cashier ini merupakan sistem kasir self-service untuk sebuah toko. Pengguna atau pembeli bisa memasukkan item yang akan dibeli, jumlah pembelian termasuk harganya. Selain itu, di dalam sistem ini juga dimasukkan fitur untuk mengubah pembelian seperti menghapus item, update nama, jumlah dan harga barang yang akan dibeli.

## Objektif
Membuat sistem self-service kasir sederhana dengan Object Oriented Programming bahasa Python  dengan class Transaction. Alur Kerja sistemnya sebagai berikut:
1. Pembeli akan membuka program dan menjalankan modul Transaksi dari script,
2. Pembeli dapat memasukkan nama item, jumlah item dan harga per item,
3. Jika pembeli akan mengubahan data pembelian, terdapat fungsi antara lain
   1. Mengubah nama barang,
   2. Mengubah jumlah barang,
   3. Mengubah harga barang,
4. Menghapus barang yang sudah diinput sebelumnya,
5. Menghapus seluruh transaksi,
6. Pembeli bisa melakukan cek transaksi untuk memastikan pembelian sudah sesuai atau belum,
7. Menghitung total belanja dan total yang harus dibayar setelah dipotong diskon jika ada.

## Flowchart
![cek](https://user-images.githubusercontent.com/114964220/205862198-bded70c4-2d06-4983-911d-f9fa942de0e3.jpg)

## Penjelasan Code
Keseluruhan Code ditulis dalam bahasa python, dalam project kali ini menggunakan class `Transaction` dan data-data dalam transaksi pembelian disimpan dengan bentuk `dictionary` dengan nama `shoppingcart`. Beberapa potongan code function atau method yang ada di class `Transaction` sesuai requirement antara lain

### Method add_item
Untuk memasukkan item barang yang akan dibeli, digunakan method `add_item`. Pembeli akan menginput nama barang, jumlah barang dan harga barang. Parameter item berupa type data string yang digunakan sebagai key dalam dict `shoppingcart`.
```
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
```
Di sini akan dicek apakah type data untuk masing-masing inputan sudah sesuai atau belum. Jika belum akan muncul peringatan menggunakan branching, tetapi jika sudah sesuai akan dimasukkan ke dalam dictionary `shoppingcart`.

### Method update_item
Ketika pembeli ingin merubah nama barang yang sudah diinput sebelumnya, makan digunakan method `update_item`
```
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
```
Dalam method ini terdapat `try` dan `except` untuk membantu validasi apakah nama barang yang akan diganti, sebelumnya sudah ada atau tidak dalam dictionary `shoppingcart`. Jika sudah sesuai maka nama barang di dictionary `shoppingcart` akan diupdate. Ditambahkan juga perintah `self.check_transaksi` untuk memunculkan dictionary dalam bentuk tabel agar memudahkan pembeli melihat daftar pembelian yang sudah diinput sebelumnya.

### Method update_quantity
Berfungsi untuk mengganti jumlah barang pembelian yang sudah diinput pembeli sebelumnya. 
```
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
 ```
 Di method ini pembeli memasukkan item yang akan diganti jumlahnya dan memasukkan jumlah baru. Terdapat `try` dan `except` untuk membantuk validasi item yang dimasukkan ada di dalam dictionary. Jika sudah sesuai, jumlah yang baru akan diupdate ke dictionary `shoppingcart` sesuai nama itemnya.
 
 ###Method update_price
 
