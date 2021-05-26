
#!/usr/bin/env python3
# -*- coding: utf8 -*-

texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae ligula quis ligula +55(55)3226-6421 efficitur feugiat. Suspendisse sapien tellus, lacinia in iaculis quis, vulputate vel felis. Proin convallis urna mauris, vitae pharetra diam finibus sed. Sed lectus risus, feugiat non mauris quis, ullamcorper vulputate purus. Vestibulum arcu nulla, luctus at tempus at, placerat u +55(55)3226-6422 t quam. Quisque ut tristique leo. Pellentesque tempus ex nibh, eu laoreet lacus fermentum ac. Sed ut pellentesque lacus. Nam sapien orci, posuere ultricies turpis sed, ultrices porta quam. Phasellus felis est, gravida efficitur aliquet vel, convallis ac ipsum. Quisque finibus mi ex, id ultricies libero interdum vitae. Etiam vestibulum odio at nisl vulputate condimentum. Vivamus viverra diam et risus interdum egestas. Pellentesque eget laoreet lectus. +55(55)3226-6423

Donec laoreet ante placerat tortor ultrices, sit amet pretium ante efficitur. Donec congue quam purus, luctus interdum lorem lacinia a. Cras imperdiet purus sed orci posuere cursus. +55(55)3226-6424 Suspendisse porttitor sollicitudin ipsum, eget vestibulum diam mattis nec. Fusce luctus nec erat eu mattis. Donec imperdiet ut odio ac dapibus. In sit amet rutrum leo, accumsan blandit neque. Donec bibendum convallis sodales. +55(55)3226-6425

Cras maximus blandit arcu, quis aliquet tortor gravida quis. Proin eget pulvinar mi.+55(55)3226-6427 Maecenas quis massa dapibus odio convallis rutrum. Pellentesque tincidunt urna quis volutpat ultrices. Ut convallis eros sit amet tempus vehicula. In est sapien, volutpat in sapien dapibus, +55(55)3226-6428 ultrices maximus est. Sed euismod viverra massa a finibus. Pellentesque quam orci, ultrices nec fringilla ut, sagittis semper quam. Fusce consequat congue sem, id cursus nulla laoreet quis. Fusce gravida a ex sit amet congue. +55(55)3226-6429 Vestibulum eu lectus nec enim aliquet feugiat placerat vitae nibh. Proin placerat, velit in efficitur suscipit, mi mi feugiat purus, sed interdum lorem ligula id dui. Aliquam erat volutpat. Donec eu ex sed tellus mattis condimentum. Vestibulum iaculis quam nec faucibus venenatis. Curabitur pulvinar, sem id lacinia condimentum, purus est accumsan lorem, sed mollis quam nunc bibendum est.+55(55)3226-6430

Aenean luctus varius diam et convallis.+55(55)3226-6431 Phasellus pulvinar risus in ligula malesuada hendrerit. Pellentesque tempor nisl erat, +55(55)3226-6432 nec dignissim tellus vestibulum at. Ut ultrices, velit non pretium rhoncus, felis massa ornare orci, ac vulputate magna sapien nec augue. +55(55)3226-6433 Proin quis felis et metus commodo sagittis. Pellentesque nec efficitur odio. Maecenas condimentum lectus at lacus aliquet,+55(55)3226-6434 sit amet bibendum quam molestie. Curabitur nisl sapien, convallis a orci id, convallis laoreet urna. Praesent eu condimentum tortor. Praesent vehicula est luctus enim auctor dapibus.+55(55)3226-6435 '''

def procuraTelefone(texto):

    if len(texto) != 16:
        return False

    if texto[0] != '+':
        return False

    for i in range(1, 3):
        if not texto[i].isdecimal():
            return False 

    if texto[3] != '(':
            return False

    for i in range(4, 6):
        if not texto[i].isdecimal():
            return False
    
    if texto[6] != ')':
            return False

    for i in range(7, 11):
        if not texto[i].isdecimal():
            return False

    if texto[11] != '-':
            return False

    for i in range(12, 16):
        if not texto[i].isdecimal():
            return False

    return True


for i in range(len(texto)):
    check = texto[i:i+16]
    if procuraTelefone(check):
        print('Telefone encontrado: ' + check)
