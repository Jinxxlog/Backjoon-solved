def solution(skill, skill_trees):
    cnt = 0
    
    for i in skill_trees:
        skname = ''.join([j for j in i if j in skill])
        
        if skill.startswith(skname):
            cnt += 1
        
    return cnt