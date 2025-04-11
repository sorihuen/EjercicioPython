# src/intermediate/databases/queries.py

def get_top_local_goal_teams():
    """Equipos con más goles locales fundados antes del año 2000"""
    return """
    SELECT 
        e.nombre AS equipo,
        SUM(p.goles_local) AS total_goles_locales
    FROM 
        Equipos e
    JOIN 
        Partidos p ON e.id_equipo = p.id_local
    WHERE 
        e.año_fundacion < 2000
    GROUP BY 
        e.id_equipo, e.nombre
    ORDER BY 
        total_goles_locales DESC
    LIMIT 2;
    """

def get_matches_with_most_goals():
    """Partidos con más goles (mostrar nombres de equipos)"""
    return """
    SELECT 
        el.nombre AS equipo_local,
        ev.nombre AS equipo_visitante,
        p.goles_local,
        p.goles_visitante,
        (p.goles_local + p.goles_visitante) AS total_goles
    FROM 
        Partidos p
    JOIN 
        Equipos el ON p.id_local = el.id_equipo
    JOIN 
        Equipos ev ON p.id_visitante = ev.id_equipo
    ORDER BY 
        total_goles DESC
    LIMIT 3;
    """

def get_teams_with_home_wins():
    """Equipos que han ganado partidos como locales"""
    return """
    SELECT 
        e.nombre AS equipo_local,
        COUNT(*) AS partidos_ganados
    FROM 
        Partidos p
    JOIN 
        Equipos e ON p.id_local = e.id_equipo
    WHERE 
        p.goles_local > p.goles_visitante
    GROUP BY 
        e.nombre
    ORDER BY 
        partidos_ganados DESC;
    """

def get_player_current_team(player_id):
    """Obtiene el equipo actual de un jugador"""
    return """
    SELECT 
        j.nombre AS jugador,
        e.nombre AS equipo_actual,
        e.id_equipo
    FROM 
        Jugadores j
    JOIN 
        Equipos e ON j.id_equipo = e.id_equipo
    WHERE 
        j.id_jugador = %s;
    """
