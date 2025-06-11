def obstacles_separe(points, distance_threshold=1.0):
    clusters = []
    for point in points:
        added = False
        for cluster in clusters:
            for clustered_point in cluster:
                dx = point[0] - clustered_point[0] 
                dy = point[1] - clustered_point[1]
                dist = (dx * dx + dy * dy) ** 0.5 # Calculate the Euclidean distance
                if dist < distance_threshold:# If the distance is less than the threshold, add the point to the cluster
                    cluster.append(point)
                    added = True
                    break
            if added:
                break
        if not added:
            clusters.append([point])
    return clusters