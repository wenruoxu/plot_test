from graphviz import Digraph

dot = Digraph(comment='Optimized Flowchart')

# 横向布局 + 正交线条
dot.attr(rankdir='LR', splines='ortho', nodesep='1.0', ranksep='1.0')
dot.attr('node', shape='ellipse', fontsize='12')
dot.attr('edge', fontsize='10')

# 添加节点
dot.node('A', 'Start')
dot.node('B', 'Process')
dot.node('C', 'Decision')
dot.node('D', 'End')

# 添加边
dot.edge('A', 'B', label='step 1')
dot.edge('B', 'C', label='step 2')
dot.edge('C', 'D', label='Yes')
dot.edge('C', 'B', label='No',)

# 渲染
dot.render('flowchart_optimized.gv', view=True)
