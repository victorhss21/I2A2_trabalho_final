"""
Gerenciamento de configuração via YAML.
"""
import yaml
import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class SystemConfig:
    """Configuração centralizada do sistema"""
    
    # Diretórios
    uploads_dir: str
    chunks_dir: str
    index_dir: str
    results_dir: str
    
    # PDF Processing
    enable_ocr: bool
    pages_per_chunk: int
    
    # Indexing
    embedding_model: str
    normalize_embeddings: bool
    
    # Extraction
    llm_model: str
    temperature: float
    max_workers: int
    rate_limit: int
    max_context_chars: int
    
    # Export
    export_json: bool
    export_excel: bool
    excel_max_desc_len: int
    
    # Logging
    log_level: str

    @classmethod
    def from_yaml(cls, yaml_path: str) -> 'SystemConfig':
        """Carrega configuração de arquivo YAML"""
        
        # Constrói o caminho absoluto a partir do local deste arquivo
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        # Navega para o diretório raiz do projeto (subindo dois níveis: core -> src -> raiz)
        project_root = os.path.join(base_dir, '..', '..')
        # Constrói o caminho completo para o arquivo de configuração
        absolute_yaml_path = os.path.join(project_root, yaml_path)
    
        with open(absolute_yaml_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
            
        return cls(
            uploads_dir=config_data['directories']['uploads'],
            chunks_dir=config_data['directories']['chunks'],
            index_dir=config_data['directories']['index'],
            results_dir=config_data['directories']['results'],
            enable_ocr=config_data['pdf_processing']['enable_ocr'],
            pages_per_chunk=config_data['pdf_processing']['pages_per_chunk'],
            embedding_model=config_data['indexing']['model'],
            normalize_embeddings=config_data['indexing']['normalize_embeddings'],
            llm_model=config_data['extraction']['llm_model'],
            temperature=config_data['extraction']['temperature'],
            max_workers=config_data['extraction']['max_workers'],
            rate_limit=config_data['extraction']['rate_limit_per_minute'],
            max_context_chars=config_data['extraction']['max_context_chars'],
            export_json=config_data['export']['formats']['json'],
            export_excel=config_data['export']['formats']['excel'],
            excel_max_desc_len=config_data['export']['excel_max_description_length'],
            log_level=config_data['logging']['level']
        ) 
