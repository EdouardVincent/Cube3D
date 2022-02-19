import rhinoscriptsyntax as rs

points = {}

for i in range(20) :
    for j in range(20):
        for k in range(20) :
            x=i*5
            y=j*5
            z=k*5
            
            points[i,j,k] = (x,y,z)

    
for i in range(20) :
    for j in range(20):
        for k in range(20) :
            if i > 0 and j > 0 and k > 0 :
                rs.AddCurve((points[i,j,k],points[i,j-1,k],
                points[i-1,j-1,k], points[i-1,j,k], points[i,j,k],
                points[i,j,k-1], points[i-1,j,k-1], points[i-1,j,k],
                points[i-1,j,k-1], points[i-1,j-1,k-1],points[i,j-1,k-1],
                points[i,j-1,k],points[i,j-1,k-1], points[i,j,k-1],
                points[i,j-1,k-1], points[i-1,j-1,k-1], points[i-1,j-1,k]),1)
            