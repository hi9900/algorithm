def solution(genres, plays):
    N = len(genres)
    
    # 장르 별 재생 횟수
    genresPlay = {}
    # 장르 별 고유 번호
    genresSong = {}
    
    for i in range(N):
        if genres[i] in genresPlay:
            genresPlay[genres[i]] += plays[i]
            genresSong[genres[i]] += [(i, plays[i])]
            
        else:
            genresPlay[genres[i]] = plays[i]
            genresSong[genres[i]] = [(i, plays[i])]
    
    maxGenresPlay = sorted(genresPlay.items(), key=lambda x: -x[1])
    result = []
    for g, _ in maxGenresPlay:
        for i, _ in sorted(genresSong[g], key=lambda x: (-x[1], x[0]))[:2]:
            result += [i]
            
    return result
    