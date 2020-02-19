#file ini berfungsi untuk memanggil fungsi "XML" odoo yang lainnya
{
    #Nama addons
    'name'          :   "Latihan addon Academic Odoo",
    #Versi Addons  
    'version'       :   "1.0",
    #List/array biasa  untuk memanggil fungsi yang ada di odoo                          
    'depends'       :   ["base", "account"],
    #Pembuat            
    'author'        :   "Rizky Lazuardi",                
    #Category untuk mencari di dalam odoo
    'category'      :   "Education",
    #Website pembuat                    
    'website'       :   "https://fujicon-japan.com/",
    #memanggil data xml
    'data'          :   [
                        "menu.xml",
                        ],
    #Deskripsi
    'description'   :   "ujicoba pembuatan addon",                              
}