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
 Di method ini pembeli memasukkan item yang akan diganti jumlahnya dan memasukkan jumlah baru. Terdapat `try` dan `except` untuk membantu validasi item yang diinput ada di dalam dictionary atau tidak. Jika sudah sesuai, jumlah yang baru akan diupdate ke dictionary `shoppingcart` sesuai nama itemnya dan menampilkan tabel pembelian yang terupdate.
 
 ### Method update_price
 Method ini berfungsi untuk mengubah harga barang yang sebelumnya sudah diinput oleh pembeli di awal. 
 ```
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
```
Di method ini pembeli memasukkan item yang akan diganti harganya dan memasukkan harga baru. Terdapat `try` dan `except` untuk membantu validasi item yang diinput ada di dalam dictionary atau tidak. Jika sudah sesuai, jumlah yang baru akan diupdate ke dictionary `shoppingcart` sesuai nama itemnya dan menampilkan tabel pembelian yang terupdate.

### Method delete_item
Saat pembeli ingin menghapus pembelian barang yang sudah diinput sebelumnya, digunakan method `delete_item`.
```
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
```
Di method ini pembeli memasukkan item yang akan dihapus. Terdapat `try` dan `except` untuk membantu validasi item yang diinput ada di dalam dictionary atau tidak. Jika sudah sesuai, item barang, jumlah serta harga yang sebelumnya sudah terinput di dictionary `shoppingcart` akan dihapus, selanjutnya akan ditampilkan tabel pembelian yang terupdate.

### Method reset_transaksi
Saat pembeli ingin menghapus semua transaksi yang sudah diinput sebelumnya, digunakan method `reset_transaksi`.
```
def reset_transaksi(self):
        '''fungsinya untuk menghapus semua data pembelian'''
        
        self.shoppingcart.clear()
        print('Semua pembelian berhasil dihapus')
```
Di method ini, seluruh pembelian yang tersimpan di dictionary `shoppingcart` akan terhapus semua.

### Method check_transaksi
Untuk mengecek apakah transaksi yang dilakukan sudah sesuai atau belum, pembeli akan menggunakan method `check_transaksi`. Method ini juga digunakan di dalam method lain untuk menampilkan tabel terupdate setelah ada update jumlah atau harga atau ketika ada item yang dihapus.
```
def check_transaksi(self):
        '''fungsinya mengecek keseluruhan pembelian yang tersimpan di dictionary transaksi.'''
        
        if self.shoppingcart == dict():
            print('Belum ada pembelian.')
        
        else:
            table_transaksi = pd.DataFrame(self.shoppingcart).T
            headers = ['Nama Barang', 'Jumlah', 'Harga per pcs', 'Total Harga']
            print(tabulate(table_transaksi, headers, tablefmt="github"))
    
```

### Method total_transaksi
Setelah semua transaksi sesuai dengan keinginan pembeli, method `total_transaksi` digunakan untuk menghitung total harga pembelian serta diskon dan harga setelah dipotong diskon jika ada.
```
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
        print(f'Total harga yang harus anda bayar setelah dipotong diskon (jika ada) sebesar Rp {total_price_discounted}'
```
Ketentuan diskon yang didapat pembeli yaitu
* Pembelian kurang dari Rp 200000 tidak mendapat diskon,
* Pembelian di atas Rp 200000 mendapat diskon 5%,
* Pembelian di atas Rp 300000 mendapat diskon 8%,
* Pembelian di atas Rp 500000 mendapat diskon 10%.

## Test Case
Untuk mengecek apakah aplikasi sederhana kasir self-service sesuia requirements atau belum maka akan dicoba menggunakan beberapa test case sebagai berikut

1. Test Case 1
Pembeli ingin menambahkan 2 item baru menggunakan metode `add_item()`. Item yang ingin ditambahkan adalah
* Nama Item : Ayam Goreng, Qty 2, Harga 20000
* Nama Item : Pasta Gigi, Qty 3, Harga 15000
Perintah yang harus dimasukkan dan outputnya akan seperti berikut
![image](https://user-images.githubusercontent.com/114964220/205926999-41505eb2-f91f-49f4-9700-3bcd0f10963a.png)

2. Test Case 2
Pembeli ingin menghapus item Pasta Gigi yang sudah diinput sebelumnya. 
Perintah yang harus dimasukkan dan outputnya akan seperti berikut
![image](https://user-images.githubusercontent.com/114964220/205927203-6b9824c9-b986-43fa-b961-b4de63403855.png)

3. Test Case 3
Pembeli ingin menghapus semua item karena kesalahan input dengan reset transaksi.
Perintah yang harus dimasukkan dan outputnya akan seperti berikut
![image](https://user-images.githubusercontent.com/114964220/205927333-7d84b73d-45b2-49b1-a414-c54f2d02f9e8.png)

4. Test Case 4
Setelah pembeli selesai berbelanja, akan menghitung total yang harus dibayarkan menggunakan method `total_price()`.
Perintah yang harus dimasukkan dan outputnya akan seperti berikut
![image](https://user-images.githubusercontent.com/114964220/205927479-30fc4ee5-ae17-4781-98f6-4e004ffd4c9e.png)
