def centres_proches_robot(clusters, robot_pos, nb_points=15):
    centres = []
    rx, ry = robot_pos
    
    for cluster in clusters:
        # Calculer la distance de chaque point au robot
        points_tries = sorted(cluster, key=lambda p: ((p[0] - rx)**2 + (p[1] - ry)**2)**0.5)
        
        # Prendre les nb_points les plus proches
        points_selectionnes = points_tries[:nb_points]
        
        # Calculer la moyenne des points sélectionnés
        x_moyen = sum(p[0] for p in points_selectionnes) / len(points_selectionnes)
        y_moyen = sum(p[1] for p in points_selectionnes) / len(points_selectionnes)
        
        centres.append((x_moyen, y_moyen))
    centre_proche = min(centres, key=lambda c: ((c[0] - rx)**2 + (c[1] - ry)**2)**0.5)
    return centre_proche