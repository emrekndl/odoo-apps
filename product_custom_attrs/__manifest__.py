# -*- coding: utf-8 -*-
{
    "name": "Product Custom Fields",
    "summary": "Product Custom Fields Module",
    "description": """ 
Odoo17 CE veya Odoo16 CE sürümünde çalıştırılan Ürün kartına 3 adet alan ekleyerek bunları Kanban ve ağaç görünümüne eklemeyi istiyorum.
Alanlarımız:
Tedarikçi Kodu Char bir alan sadece Sayı değeri alacaksa harf girildiyse gösterecek bir Mekanizma.
İşaretleme alanı float bir değer alacak 0 dan küçük olduğunda hata verecektir.
QRCODE : Binary bir alan bu kanbanda değil ağaç ve formda olacak. bu alan tedarikçisinin referansından hesaplanıp gelecek. Bu alandan itibaren tedarikçi referansı değişti.
    """,
    "author": "emrekndl",
    "website": "kondulemre@gmail.com",
    "category": "Sales",
    "version": "0.1",
    "sequence": "1",
    "depends": ["base", "sale"],
    "external_dependencies": {
        "python": ["qrcode"],
    },
    "data": [
        # 'security/ir.model.access.csv',
        "views/inherit_product_template_view.xml",
        "views/inherit_product_product_view.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": False,
}
