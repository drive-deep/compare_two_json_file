def compare(f1,f2,file,i):
    for x in f1:
        if x not in f2:
            if file not in not_equal:
                not_equal.append(file)
            print(x,"not present in ",file,i)

        elif isinstance(f1[x],dict) and isinstance(f2[x],dict):
            compare(f1[x],f2[x],file,i)


        elif f1[x]!=f2[x]:
            print("value is not same for key:",x ,"in file ",file,i)
            print("dev:",f1[x],"jsonmapper_sumter:",f2[x])

            if file not in not_equal:
                not_equal.append(file)
