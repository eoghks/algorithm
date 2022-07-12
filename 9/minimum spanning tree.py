import load as ld
import prim as pr
import kruskal as kr
#graph ㅣ입력
graph=ld.load()
#prim
primF=pr.prim(graph)
print("prinm spanning tree : ",primF)
#kruskal
kruskalF=kr.kruskal(graph)
print("kruskal spanning tree : ",kruskalF)
#cmd자동종료
input("종료하시려면 Enter키를 눌러주세요.")
