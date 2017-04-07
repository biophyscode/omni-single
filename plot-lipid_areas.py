#!/usr/bin/env python

"""
PLOT MESH OBJECTS
plots that derive from the Delaunay mesh objects generated by codes/mesh.py
"""

routine = ['review3d','cellplot'][:1]

#---load everything
if 'data' not in globals(): 
	data,calcs = plotload(plotname,work)
	data_prot,calcs_prot = plotload('protein_abstractor',work)

if 'review3d' in routine:

	import mayavi
	from mayavi import mlab
	from codes.review3d import review3d,pbcbox

	sn = 'mk004'
	dat = data[sn]['data']
	mn,fr = 1,10
	pts = dat['%d.%d.%s'%(mn,fr,'points')]
	vec = dat['%d.%d.%s'%(mn,fr,'vec')]
	mean_curvs = dat['%d.%d.%s'%(mn,fr,'mean')]
	mean_curvs_normed = mean_curvs/np.abs(mean_curvs).max()+0.5
	review3d(points=[pts],tube=0.02,radius=0.2,noshow=True,colorset=mean_curvs_normed,cmap='seismic')
	review3d(points=data_prot[sn]['data']['points_all'][fr],radius=0.4,noshow=True)
	pbcbox(vec)
	mlab.show()
	
if 'cellplot' in routine:

	from codes.cellplot import cellplot

	sn = 'mk002'
	dat = data[sn]['data']
	mn,fr = 1,10
	simps = dat['%d.%d.simplices'%(mn,fr)]
	pts = dat['%d.%d.points'%(mn,fr)]
